using System;
using Server.Items;
using Server.Mobiles;

namespace Server.Mobiles
{
	[CorpseName( "a Tsuki Wolf corpse" )]
	public class TsukiWolf : BaseCreature
	{
		public override WeaponAbility GetWeaponAbility()	
            {
                  return WeaponAbility.BleedAttack;
            } 

		[Constructable]
		public TsukiWolf() : base( AIType.AI_Melee, FightMode.Closest, 10, 1, 0.2, 0.4 )
		{
			Name = "a Tsuki Wolf";
			Body = 250;
			BaseSoundID = 0xE5;

			SetStr( 400, 450 );
			SetDex( 150, 200 );
			SetInt( 65, 75 );

			SetHits( 380, 440 );
			SetMana( 40, 40 );
			SetStam( 150, 200 );

			SetDamage( 48, 73 );

			SetDamageType( ResistanceType.Physical, 90 ); 
	         	SetDamageType( ResistanceType.Cold, 5 ); 
        	 	SetDamageType( ResistanceType.Energy, 5 ); 

			SetResistance( ResistanceType.Physical, 40, 60 );
			SetResistance( ResistanceType.Fire, 50, 70 );
			SetResistance( ResistanceType.Cold, 50, 70 );
			SetResistance( ResistanceType.Poison, 50, 70 );
			SetResistance( ResistanceType.Energy, 50, 70 );

			SetSkill( SkillName.MagicResist, 65.0, 70.0 );
			SetSkill( SkillName.Tactics, 95.0, 110.0 );
			SetSkill( SkillName.Wrestling, 98.0, 108.0 );
			SetSkill( SkillName.Anatomy, 65.0, 75.0 );

			Fame = 15000;
			Karma = 15000;
			
			Tamable = false;

         PackGold( 400, 500 ); 
         PackMagicItems( 1, 5 );
		 PackItem( new Bone( Utility.RandomMinMax( 5, 14 ) ));
		 PackReg( 5, 14 );
		 //TODO: Pack Bodyparts
 
		}
		
		public override void GenerateLoot()
		{
			AddLoot( LootPack.MedScrolls, 1 );
			AddLoot( LootPack.Rich );
		}

		public override bool CanRummageCorpses{ get{ return true; } }
		public override int Meat{ get{ return 4; } }
		public override int Hides{ get{ return 25; } }
		public override HideType HideType{ get{ return HideType.Spined; } }
		public override FoodType FavoriteFood{ get{ return FoodType.Meat; } }
		public override PackInstinct PackInstinct{ get{ return PackInstinct.Canine; } }

                public TsukiWolf( Serial serial ) : base( serial )
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