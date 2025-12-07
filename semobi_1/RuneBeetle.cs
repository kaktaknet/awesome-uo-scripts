using System;
using Server.Items;
using Server.Mobiles;

namespace Server.Mobiles
{
	[CorpseName( "a rune beetle corpse" )]
	public class RuneBeetle : BaseCreature
	{
		public override WeaponAbility GetWeaponAbility()	
            {
                  return WeaponAbility.BleedAttack;
            } 

		[Constructable]
		public RuneBeetle() : base( AIType.AI_Mage, FightMode.Closest, 10, 1, 0.2, 0.4 )
		{
			BaseSoundID = 0x4E8;

			Name = "Rune Beetle";
			Body = 244;
			
			SetStr( 400, 450 );
			SetDex( 125, 170 );
			SetInt( 375, 450 );

			SetHits( 310, 360 );
			SetMana( 375, 450 );
			SetStam( 125, 170 );

			SetDamage( 42, 60 );

			SetDamageType( ResistanceType.Physical, 20 ); 
         	SetDamageType( ResistanceType.Poison, 10 ); 
         	SetDamageType( ResistanceType.Energy, 70 ); 

			SetResistance( ResistanceType.Physical, 40, 65 );
			SetResistance( ResistanceType.Fire, 35, 50 );
			SetResistance( ResistanceType.Cold, 35, 50 );
			SetResistance( ResistanceType.Poison, 75, 95 );
			SetResistance( ResistanceType.Energy, 40, 60 );

			SetSkill( SkillName.MagicResist, 95.0, 110.0 );
			SetSkill( SkillName.Tactics, 80.0, 95.0 );
			SetSkill( SkillName.Wrestling, 70.0, 80.0 );
			SetSkill( SkillName.Poisoning, 120.0, 140.0 );
			SetSkill( SkillName.Magery, 100.0, 110.0 );
			SetSkill( SkillName.Meditation, 95.0, 110.0 );
			SetSkill( SkillName.EvalInt, 100.0, 125.0 );

			Fame = 15000;
			Karma = -15000;
			
			Tamable = true;
			ControlSlots = 3;
			MinTameSkill = 93.9;
			
         PackGold( 1000, 1200 ); 
         PackMagicItems( 1, 5 );
		 PackItem( new Bone( Utility.RandomMinMax( 5, 14 ) ));
		 PackReg( 5, 14 );
		 //TODO: Pack Bodyparts
 
		}
		
		public override void GenerateLoot()
		{
			AddLoot( LootPack.MedScrolls, 1 );
		}
		public override Poison PoisonImmune{ get{ return Poison.Deadly; } }
		public override Poison HitPoison{ get{ return Poison.Deadly; } }
      	public override bool BardImmune{ get{ return true; } }
		public override FoodType FavoriteFood{ get{ return FoodType.FruitsAndVegies; } }

                public RuneBeetle( Serial serial ) : base( serial )
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