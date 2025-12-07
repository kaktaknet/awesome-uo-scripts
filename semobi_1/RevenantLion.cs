using System;
using Server.Items;
using Server.Mobiles;

namespace Server.Mobiles
{
	[CorpseName( "a Revenant Lion corpse" )]
	public class RevenantLion : BaseCreature
	{
		public override WeaponAbility GetWeaponAbility()	
            {
                  return WeaponAbility.BleedAttack;
            } 

		[Constructable]
		public RevenantLion() : base( AIType.AI_Melee, FightMode.Closest, 10, 1, 0.2, 0.4 )
		{
			Name = "a Revenant Lion";
			Body = 251;
			BaseSoundID = 0xBA;

			SetStr( 275, 320 );
			SetDex( 155, 175 );
			SetInt( 75, 105 );

			SetHits( 250, 280 );
			SetMana( 75, 105 );
			SetStam( 155, 175 );

			SetDamage( 42, 58 );

			SetDamageType( ResistanceType.Physical, 30 ); 
 	        	SetDamageType( ResistanceType.Poison, 10 ); 
 	        	SetDamageType( ResistanceType.Cold, 30 ); 
        	 	SetDamageType( ResistanceType.Energy, 30 ); 

			SetResistance( ResistanceType.Physical, 40, 60 );
			SetResistance( ResistanceType.Fire, 20, 30 );
			SetResistance( ResistanceType.Cold, 50, 60 );
			SetResistance( ResistanceType.Poison, 55, 65 );
			SetResistance( ResistanceType.Energy, 40, 50 );

			SetSkill( SkillName.MagicResist, 70.0, 80.0 );
			SetSkill( SkillName.Tactics, 60.0, 80.0 );
			SetSkill( SkillName.Wrestling, 80.0, 90.0 );
			SetSkill( SkillName.Poisoning, 120.0, 130.0 );
			SetSkill( SkillName.Magery, 80.0, 90.0 );
			SetSkill( SkillName.Meditation, 85.0, 95.0 );
			SetSkill( SkillName.EvalInt, 80.0, 90.0 );

			Fame = 2500;
			Karma = 2500;
			
			Tamable = false;

         PackGold( 550, 700 ); 
         PackMagicItems( 1, 5 );
		 PackItem( new Bone( Utility.RandomMinMax( 5, 14 ) ));
		 PackReg( 5, 14 );
		 //TODO: Pack Bodyparts
 
		}
		
		public override void GenerateLoot()
		{
			AddLoot( LootPack.MedScrolls, 1 );
		}
		public override Poison PoisonImmune{ get{ return Poison.Greater; } }
		public override Poison HitPoison{ get{ return Poison.Greater; } }
		public override FoodType FavoriteFood{ get{ return FoodType.Meat; } }
		public override PackInstinct PackInstinct{ get{ return PackInstinct.Feline; } }

                public RevenantLion( Serial serial ) : base( serial )
		{
		}

		public override void Serialize( GenericWriter writer )
		{
			base.Serialize( writer );

			writer.Write( (int) 0 ); // version
		}

		public override void Deserialize( GenericReader reader )
		{
			base.Deserialize( reader );

			int version = reader.ReadInt();
		}
	}
}